import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { environment } from 'src/environments/environment';
import { Dashboard } from 'src/app/_models/dashboard';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

@Injectable({ providedIn: 'root' })
export class DashboardService {
    constructor(private http: HttpClient) { }

    getdashboardDetails() {
        return this.http.get(`${environment.apiUrl}/auth/dashboard`);
    }

}