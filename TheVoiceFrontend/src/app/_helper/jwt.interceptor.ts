import { Injectable } from '@angular/core';
import { HttpRequest, HttpHandler, HttpEvent, HttpInterceptor } from '@angular/common/http';
import { Observable } from 'rxjs';

import { AuthenticationService } from 'src/app/_services/authentication.service';

@Injectable()
export class JwtInterceptor implements HttpInterceptor {
    constructor(private authenticationService: AuthenticationService) { }

    intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
        // add authorization header 
        let currentUser = this.authenticationService.currentUserValue;
        let currentToken = this.authenticationService.currentTokenValue;
        if (currentToken.access) {
            console.log(currentToken.access);
            
            request = request.clone({
                setHeaders: {
                    Authorization: `Bearer ${currentToken.access}`
                }
            });
        }

        return next.handle(request);
    }
}