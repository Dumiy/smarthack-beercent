import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators, AbstractControl } from '@angular/forms';
import { AuthenticationService } from 'src/app/api/services';
import { Router } from '@angular/router';
import { MatDialogRef } from '@angular/material/dialog';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  EMAIL_CONTROL_NAME: string = 'email';
  PASSWORD_CONTROL_NAME: string = 'password';
  loginFormGroup: FormGroup;

  get emailControl(): AbstractControl {
    return this.loginFormGroup.get(this.EMAIL_CONTROL_NAME);
  }

  get passwordControl(): AbstractControl {
    return this.loginFormGroup.get(this.PASSWORD_CONTROL_NAME);
  }

  constructor(private formBuilder: FormBuilder,
            private dialogRef: MatDialogRef<LoginComponent>,
            private router: Router,
            private snackbar: MatSnackBar,
            private authenticationService: AuthenticationService) { }

  ngOnInit(): void {
    this.intializeLoginFormGroup();
  }

  intializeLoginFormGroup(): void {
    this.loginFormGroup = this.formBuilder.group({
      [this.EMAIL_CONTROL_NAME]: ['', [Validators.required]],
      [this.PASSWORD_CONTROL_NAME]: ['', [Validators.required]]
    });
  }

  close(): void {
    this.dialogRef.close();
  }

  submit(): void {
    if (this.loginFormGroup.invalid) {
        return;
    }
    this.authenticationService.login(
      this.emailControl.value,
      this.passwordControl.value
    ).subscribe(
      () => {
        this.dialogRef.close();
        this.router.navigate(['/find']);
      },
      (error) => {
        this.snackbar.open('Your credentials may be invalid!', 'Close', {
          duration: 2000
        });
      }
    )
}

}
