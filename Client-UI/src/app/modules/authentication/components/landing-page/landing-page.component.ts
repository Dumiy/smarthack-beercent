import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthenticationService } from 'src/app/api/services';
import { MatDialog } from '@angular/material/dialog';
import { LoginComponent } from '..';
import { RegisterComponent } from '../register/register.component';

@Component({
  selector: 'app-landing-page',
  templateUrl: './landing-page.component.html',
  styleUrls: ['./landing-page.component.scss']
})
export class LandingPageComponent implements OnInit {

  constructor(private matDialog: MatDialog,
              private authenticationService: AuthenticationService) { }

  ngOnInit(): void {
  }

  openLoginDialog(): void {
    this.matDialog.open(LoginComponent, {
      minHeight: 250,
      minWidth: 350
    })
  }

  openRegisterDialog(): void {
    this.matDialog.open(RegisterComponent, {
      minHeight: 250,
      minWidth: 350
    })
  }

}
