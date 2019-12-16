import { BrowserModule } from '@angular/platform-browser';
import { NgModule,CUSTOM_ELEMENTS_SCHEMA  } from '@angular/core';
import { Ng2SearchPipeModule } from 'ng2-search-filter';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule,HTTP_INTERCEPTORS } from '@angular/common/http';
import { appRoutingModule } from 'src/app/app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './component/login/login.component';
import { HomeComponent } from './component/home/home.component';

import { ErrorInterceptor } from 'src/app/_helper/error.interceptor';
import { JwtInterceptor } from 'src/app/_helper/jwt.interceptor';
import { UserdetailsComponent } from './component/userdetails/userdetails.component';

@NgModule({
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
  declarations: [
    AppComponent,
    LoginComponent,
    HomeComponent,
    UserdetailsComponent
  ],
  imports: [
    BrowserModule,
    appRoutingModule,
    HttpClientModule,
    HttpClientModule,
    FormsModule, 
    ReactiveFormsModule,
    Ng2SearchPipeModule 
  ],
  providers: [
    { provide: HTTP_INTERCEPTORS, useClass: JwtInterceptor, multi: true },
    { provide: HTTP_INTERCEPTORS, useClass: ErrorInterceptor, multi: true },

    // provider used to create fake backend
],
  bootstrap: [AppComponent]
})
export class AppModule { }


