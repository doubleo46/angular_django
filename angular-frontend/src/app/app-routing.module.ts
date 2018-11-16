import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CustomersComponent } from './customers/customers.component';
import { CustomerformComponent } from './customerform/customerform.component';
import { ServiceformComponent } from './serviceform/serviceform.component';
import { TestingformComponent } from './testingform/testingform.component';

const routes: Routes = [
  {
    path:'',
    component: CustomersComponent
  },
  {
    path:'create_customer',
    component:CustomerformComponent
  },
  {
    path:'create_service',
    component:ServiceformComponent
  },
  {
    path:'testing_from',
    component:TestingformComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
