import { Component, OnInit } from '@angular/core';
import { first } from 'rxjs/operators';
import { DashboardService } from 'src/app/_services/dashboard.service';
import { Dashboard } from 'src/app/_models/dashboard';
import { AuthenticationService } from 'src/app/_services/authentication.service';

@Component({ templateUrl: 'home.component.html' })
export class HomeComponent {
    loading = false;
    dahboardDetails : any;
    dashboardelemets : any;
    constructor(private dashboardService: DashboardService) { }

    ngOnInit() {
        this.loading = true;
        this.dashboardService.getdashboardDetails().subscribe(
          data => {
            this.loading = false;
            this.dahboardDetails = data;
            this.dashboardelemets = data[0]['mentor_name'];
          },
          error => {

          });
    }
}


