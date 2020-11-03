import { Component, OnInit } from '@angular/core';
import { FormGroup, AbstractControl, FormBuilder, Validators } from '@angular/forms';
import { MatDialogRef } from '@angular/material/dialog';
import { AuthenticationService } from 'src/app/api/services';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {
  registerFormGroup: FormGroup;
  USER_NAME_CONTROL_NAME: string = 'user_name';
  EMAIL_CONTROL_NAME: string = 'email';
  PASSWORD_CONTROL_NAME: string = 'password';
  CONFIRM_PASSWORD_CONTROL_NAME: string = 'confirm_password';

  get userNameControl(): AbstractControl {
    return this.registerFormGroup.get(this.USER_NAME_CONTROL_NAME);
  }

  get emailControl(): AbstractControl {
    return this.registerFormGroup.get(this.EMAIL_CONTROL_NAME);
  }

  get passwordControl(): AbstractControl {
    return this.registerFormGroup.get(this.PASSWORD_CONTROL_NAME);
  }

  get confirmPasswordControl(): AbstractControl {
    return this.registerFormGroup.get(this.CONFIRM_PASSWORD_CONTROL_NAME);
  }
  constructor(private formBuilder: FormBuilder,
              private dialogRef: MatDialogRef<RegisterComponent>,
              private authenticationService: AuthenticationService,
              private snackbar: MatSnackBar) { }

  ngOnInit(): void {
    this.intializeRegisterFormGroup();
  }

  intializeRegisterFormGroup(): void {
    this.registerFormGroup = this.formBuilder.group({
      [this.USER_NAME_CONTROL_NAME]: ['', [Validators.required, Validators.min(4)]],
      [this.EMAIL_CONTROL_NAME]: ['', [Validators.required, Validators.min(6)]],
      [this.PASSWORD_CONTROL_NAME]: ['', [Validators.required, Validators.min(2)]],
      [this.CONFIRM_PASSWORD_CONTROL_NAME]: ['', [Validators.required, Validators.min(2)]],
    },
      { validator: this.checkPasswords.bind(this) }
    );
  }

    checkPasswords(formGroup: FormGroup) {
      const newPasswordControl: AbstractControl = formGroup.get(this.PASSWORD_CONTROL_NAME);
      const confirmPasswordControl: AbstractControl = formGroup.get(this.CONFIRM_PASSWORD_CONTROL_NAME);
      return newPasswordControl && confirmPasswordControl && newPasswordControl.value === confirmPasswordControl.value ? null : { notSame: true };
    }

    hasNotSameError(): boolean {
      console.log(this.registerFormGroup.hasError('notSame'));
      return this.registerFormGroup.hasError('notSame');
    }

  close(): void {
    this.dialogRef.close();
  }

  submit(): void {
    if (this.registerFormGroup.invalid) {
        return;
    }
    this.authenticationService.register(
      this.userNameControl.value,
      this.emailControl.value,
      this.passwordControl.value
    ).subscribe(
      () => {
        this.snackbar.open('Registration succesfully! You re now a wirer! ', 'Close', {
          duration: 2000
        });
        this.dialogRef.close();
      },
      (error) => {
        this.snackbar.open('Your credentials may be invalid!', 'Close', {
          duration: 2000
        });
      }
    );
  }
}
