import { Injectable } from '@angular/core';
import { Router, CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot } from '@angular/router';
import { AuthenticationService } from 'src/app/_services/authentication.service';

@Injectable({ providedIn: 'root' })
export class AuthGuard implements CanActivate {
    constructor(
        private router: Router,
        private authenticationService: AuthenticationService
    ) { }

    canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot) {
        const currentToken = this.authenticationService.currentTokenValue;
        if (currentToken) {
            console.log("check 03");
            // logged in 
            return true;
        }
        // not logged in redirecting to login page 
        this.router.navigate(['login'], { queryParams: { returnUrl: state.url } });
        return false;
    }
}