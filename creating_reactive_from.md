For from creaton we are going to use "angular/material"

use ng add @angular/material to get it.

append 'ReactiveFormsModule' from '@angular/forms'
create a component for the form.


What is a Reactive Form?
A reactive form is just an HTML form that’s been wired up with RxJS to manage it's state as a realtime stream.
This means you can listen to changes to it's value as an Observable and react accordingly with validation errors,
feedback, database operations, etc

FormControl - An individual form input, checkbox, select, textarea, etc.
FormGroup - A group of form fields that can be manipulated and validated together.
FormBuilder - A service that helps you build FormGroups easily.


1. Create a component to create a form(serviceForm).
2. import formGroup and FormBuilder
3. define the form.
4. create a form builder object in constructer.
5. initialize form with required varibales.
6. import HttpClientModule in app.module and add it to the import lis.
7. import HttpClient and HttpHeaders in servicefrom component
8. initialize httpclient in constructer.
9. Define post function 
10. define httpheaders
11. assign values from front end to a constant and post
12. Then in HTML in from '(ngSubmit)' import submit function
