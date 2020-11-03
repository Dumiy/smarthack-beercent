import { Injectable } from '@angular/core';
import { Router, CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot } from '@angular/router';
import { AuthenticationService } from '../../../api/services';

@Injectable({
    providedIn: 'root'
})
export class LandingGuard implements CanActivate {
    constructor(
        private router: Router,
        private authenticationService: AuthenticationService
    ) { }

    canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot) {
        const currentUser = this.authenticationService.isLoggedIn();
        if (currentUser) {

            this.router.navigate(['/find']);
            return false;
        }

        // not logged in so redirect to login page with the return url
        return true;
    }
}