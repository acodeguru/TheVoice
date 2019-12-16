import { ActivatedRoute } from '@angular/router'
import { Component, OnInit } from '@angular/core';
import { CandidateService } from 'src/app/_services/candidate.service';

@Component({
  selector: 'app-userdetails',
  templateUrl: './userdetails.component.html',
  styleUrls: ['./userdetails.component.scss']
})
export class UserdetailsComponent {
    loading = false;
    id:"";
    candidateDetails:any;

    constructor(private activeRoute: ActivatedRoute, private candidateService: CandidateService) { 
      const routeParams = this.activeRoute.snapshot.params;
      this.id=routeParams.id;
    }
    ngOnInit() {
        this.loading = true;
        this.candidateService.getcandidateDetails(this.id).subscribe(
          data => {
            this.loading = false;
            this.candidateDetails = data;
          },
          error => {

          });
    }
}


