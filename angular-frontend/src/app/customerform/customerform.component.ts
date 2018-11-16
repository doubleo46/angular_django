import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { HttpClient,HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';


@Component({
  selector: 'app-customerform',
  templateUrl: './customerform.component.html',
  styleUrls: ['./customerform.component.scss']
})
export class CustomerformComponent implements OnInit {

  customerForm: FormGroup;
  post:Observable<any>
  result:any
  constructor(private fbuilder:FormBuilder, private http:HttpClient) { }
  
  ngOnInit() {
    this.customerForm = this.fbuilder.group({
      name:'',
      age:''
    })
  }
  onSubmit() {
    // TODO: Use EventEmitter with form value
    let headers = new HttpHeaders().set('Content-Type','application/json')
    console.log(this.customerForm.value);
    const data = this.customerForm.value;
    this.result = this.http.post('http://localhost:8046/api/create_customer',data).subscribe();
    console.log(this.result)
}
}
