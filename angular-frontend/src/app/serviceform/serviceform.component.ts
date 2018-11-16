import { Component, OnInit } from '@angular/core';
import {FormBuilder, FormGroup } from '@angular/forms';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-serviceform',
  templateUrl: './serviceform.component.html',
  styleUrls: ['./serviceform.component.scss']
})
export class ServiceformComponent implements OnInit {

  serviceForm : FormGroup;
  result: any

  constructor(private fb: FormBuilder, private http:HttpClient) { }

  ngOnInit() {
    this.serviceForm = this.fb.group({
      name: '',
      description:''
    })
  }

    onSubmit(){
      const data = this.serviceForm.value;
      let headers = new HttpHeaders({
        'Content-Type': 'application/json',
        'Authorization':'auth-token'});
      let options = { headers: headers };
        
      this.result = this.http.post('http://localhost:8046/api/create_customer',{data,options}).subscribe()

    }
}
