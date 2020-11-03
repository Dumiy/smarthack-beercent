import { Component } from '@angular/core';
import { User } from './modules/shared/models';
import { Router } from '@angular/router';
import { AuthenticationService } from './api/services';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  currentUser: User;

  constructor(
      private router: Router,
      public authenticationService: AuthenticationService
  ) {
      this.authenticationService.currentUser.subscribe(x => this.currentUser = x);
  }

  logout(): void {
      this.authenticationService.logout();
      this.router.navigate(['/login']);
  }
}
