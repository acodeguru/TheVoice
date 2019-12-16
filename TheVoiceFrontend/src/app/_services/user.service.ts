import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { environment } from 'src/environments/environment';
import { User } from 'src/app/_models/user';

@Injectable({ providedIn: 'root' })
export class UserService {
    constructor(private http: HttpClient) { }

    getUserDetails() {
        let currentUser = this.http.get<User>(`${environment.apiUrl}/auth/user`);
        console.log(currentUser)
        localStorage.setItem('currentUser', JSON.stringify(currentUser));
        return currentUser
    }

}