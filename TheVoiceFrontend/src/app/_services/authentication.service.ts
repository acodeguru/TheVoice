import { Injectable } from '@angular/core';
import { HttpClient, HttpBackend, HttpParams, HttpHeaders } from '@angular/common/http';
import { BehaviorSubject, Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { environment } from 'src/environments/environment';
import { User } from 'src/app/_models/user';
import { Token } from 'src/app/_models/token';

@Injectable({ providedIn: 'root' })
export class AuthenticationService {
    private currentUserSubject: BehaviorSubject<User>;
    private currentTokenSubject: BehaviorSubject<Token>;

    public currentUser: Observable<User>;
    public currentToken: Observable<Token>;

    constructor(private http: HttpClient, private handler: HttpBackend) {
        this.currentUserSubject = new BehaviorSubject<User>(JSON.parse(localStorage.getItem('currentUser')));
        this.currentUser = this.currentUserSubject.asObservable();

        this.currentTokenSubject = new BehaviorSubject<Token>(JSON.parse(localStorage.getItem('currentToken')));
        this.currentToken = this.currentTokenSubject.asObservable();
    }

    public get currentTokenValue(): Token {
        return this.currentTokenSubject.value;
    }

    public get currentUserValue(): User {
        return this.currentUserSubject.value;
    }


    login(username: string, password: string) {
        this.http = new HttpClient(this.handler);
        const headerSet = new HttpHeaders().set('Content-Type', 'application/x-www-form-urlencoded');
        const body = new HttpParams().set('username', username).set('password', password);

        return this.http.post<any>(`${environment.apiUrl}/auth/token/`, body.toString(), { headers: headerSet }).pipe(map(token => {
            // store user details and jwt token in local storage to keep user logged in between page refreshes
            localStorage.setItem('currentToken', JSON.stringify(token));
            this.currentTokenSubject.next(token);
            return token;
        }));
    }

    logout() {
        // remove user from local storage to log user out
        localStorage.removeItem('currentUser');
        localStorage.removeItem('currentToken');
        this.currentUserSubject.next(null);
    }
}