import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { first } from 'rxjs/operators';

import { AuthenticationService } from 'src/app/_services/authentication.service';
import { UserService } from 'src/app/_services/user.service';

@Component({ templateUrl: 'login.component.html' })
export class LoginComponent implements OnInit {
    loginForm: FormGroup;
    loading = false;
    submitted = false;
    returnUrl: string;
    error = '';

    constructor(
        private formBuilder: FormBuilder,
        private route: ActivatedRoute,
        private router: Router,
        private authenticationService: AuthenticationService,
        private userService: UserService,

    ) { 
        // already logged in redirecting
        if (this.authenticationService.currentTokenValue) { 
            this.router.navigate(['/']);
        }
    }

    ngOnInit() {
        this.loginForm = this.formBuilder.group({
            username: ['', Validators.required],
            password: ['', Validators.required]
        });

        // get return url from route 
        this.returnUrl = this.route.snapshot.queryParams['returnUrl'] || '/';
    }

    // getter for easy access to form fields
    get f() { return this.loginForm.controls; }

    onSubmit() {
        this.submitted = true;

        // check if form is invalid
        if (this.loginForm.invalid) {
            return;
        }
        console.log("check 07");
        this.loading = true;
        this.authenticationService.login(this.f.username.value, this.f.password.value)
            .pipe(first())
            .subscribe(
                data => {
                  this.userService.getUserDetails().pipe(first()).subscribe(user=> {
                    console.log("check 08");
                  });

                  this.router.navigate([this.returnUrl]);

                },
                error => {
                    this.error = "Username or Password Incorrect";
                    this.loading = false;
                });
                
    }
}