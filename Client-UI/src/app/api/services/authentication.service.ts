import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { BehaviorSubject, Observable } from 'rxjs';
import { map, tap } from 'rxjs/operators';

import { environment } from '../../../environments/environment';
import { User } from '../../modules/shared/models';
import { Router } from '@angular/router';
import * as jwt_decode from "jwt-decode";

@Injectable({
    providedIn: 'root'
})
export class AuthenticationService {
    public currentUserSubject: BehaviorSubject<User>;
    public currentUser: Observable<User>;
    httpOptions = {
        headers: new HttpHeaders({'Content-Type': 'application/json'})
        // headers: new HttpHeaders({ 'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'})
      }

    loginRoute: string = '/account/createToken';
    registerRoute: string = '/account/register';

    constructor(private http: HttpClient,
                private router: Router) {
        this.currentUserSubject = new BehaviorSubject<User>(JSON.parse(sessionStorage.getItem('currentUser')));
        this.currentUser = this.currentUserSubject.asObservable();
    }

    public get currentUserValue(): User {
        return this.currentUserSubject.value;
    }

    public isLoggedIn(): boolean {
        const token = sessionStorage.getItem('currentUser');
        try {
            return !!token;
          } catch (e) {
            return false;
          }
    }

    public getUsername(): string {
        const username: string = JSON.parse(sessionStorage.getItem('username'));
        return !!username ? username : '';
    }

    register(username: string, email: string,  password: string) {
        return this.http.post(`${environment.apiUrl}${this.registerRoute}`, {
            email: email,
            username: username,
            password: password
        }, this.httpOptions);
    }

    login(email: string,  password: string) {
        return this.http.post(`${environment.apiUrl}${this.loginRoute}`, {
            email,
            password
        }, this.httpOptions).pipe(
            tap((result: any) =>  {
                sessionStorage.setItem('username', JSON.stringify(result.user.userName));
                sessionStorage.setItem('currentUser', JSON.stringify(result.token))
                this.currentUserSubject.next(result.user);
            }
        ));
    }

    logout() {
        // remove user from local storage to log user out
        sessionStorage.removeItem('currentUser');
        this.router.navigate(['/landing-page']);
        this.currentUserSubject.next(null);
    }
}