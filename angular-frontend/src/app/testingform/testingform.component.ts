import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder } from '@angular/forms';
import { HttpClient, HttpHeaders } from '@angular/common/http';
@Component({
  selector: 'app-testingform',
  templateUrl: './testingform.component.html',
  styleUrls: ['./testingform.component.scss']
})
export class TestingformComponent implements OnInit {

  testingForm:FormGroup;
  constructor(private fb:FormBuilder, private http:HttpClient) { }
  result :any;
  ngOnInit() {
    this.testingForm = this.fb.group({
      name:'',
      task:''
    })
  }
  trySubmit(){
    let headers = new HttpHeaders({
      'Content-Type':'application/json'
    })
    const data = this.testingForm.value;
    this.result = this.http.post('http://localhost:8046/api/create_customer',{data,headers}).subscribe()

  }
}
