import { Component } from '@angular/core';
import { Router, RouterStateSnapshot } from '@angular/router';

import { AuthenticationService } from 'src/app/_services/authentication.service';
import { Token } from 'src/app/_models/token';

@Component({ selector: 'app', templateUrl: 'app.component.html' })
export class AppComponent {
    title = 'TheVoiceTV';
    currentToken: Token;

    constructor(
        private router: Router,
        private authenticationService: AuthenticationService
    ) {
        this.authenticationService.currentToken.subscribe(x => this.currentToken = x);
    }

    logout() {
        this.authenticationService.logout();
        this.router.navigate(['/login/']);
        document.location.href="/";
    }
}
