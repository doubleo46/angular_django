import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SidebarComponent } from './sidebar/sidebar.component';
import { CustomerformComponent } from './customerform/customerform.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ReactiveFormsModule,FormsModule } from '@angular/forms';

import { MatInputModule } from '@angular/material/input';
import { MatSelectModule } from '@angular/material/select';
import { MatButtonModule } from '@angular/material/button';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { MatChipsModule } from '@angular/material/chips';
import { CustomersComponent } from './customers/customers.component'
import { MatFormFieldModule } from '@angular/material';
import { HttpClientModule } from '@angular/common/http';
import { ServiceformComponent } from './serviceform/serviceform.component';
import { TestingformComponent } from './testingform/testingform.component';

@NgModule({
  declarations: [
    AppComponent,
    SidebarComponent,
    CustomerformComponent,
    CustomersComponent,
    ServiceformComponent,
    TestingformComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    FormsModule,
    ReactiveFormsModule,
    MatInputModule,
    MatSelectModule,
    MatButtonModule,
    MatCheckboxModule,
    MatChipsModule,
    MatFormFieldModule,
    HttpClientModule

    

  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
