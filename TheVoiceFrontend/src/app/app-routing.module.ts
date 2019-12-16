import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './component/login/login.component';
import { HomeComponent } from './component/home/home.component';
import { UserdetailsComponent } from './component/userdetails/userdetails.component';
import { AuthGuard } from 'src/app/_helper/auth.guard';

const routes: Routes = [
  // {path: '',pathMatch: 'full',redirectTo:'/login'},
  {path: '', component: HomeComponent, canActivate: [AuthGuard] },
  {path: 'login',component: LoginComponent},
  {path: 'candidate/:id',component: UserdetailsComponent},

  // otherwise redirect to home
  { path: '**', redirectTo: '' }
];

export const appRoutingModule = RouterModule.forRoot(routes);
