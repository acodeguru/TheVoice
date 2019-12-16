import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { environment } from 'src/environments/environment';
import { Dashboard } from 'src/app/_models/dashboard';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

@Injectable({ providedIn: 'root' })
export class CandidateService {
    constructor(private http: HttpClient) { }

    getcandidateDetails(candidate_id) {
        return this.http.get(`${environment.apiUrl}/performance/candidate/`+candidate_id);
    }

}    
