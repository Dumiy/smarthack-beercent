import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from '../../../environments/environment';
import { Observable } from 'rxjs';

@Injectable({
    providedIn: 'root'
})
export class TestService {
    constructor(private http: HttpClient) {}
    testRoute: string = '/searchengine';

    testApi(): Observable<any> {
        return this.http.get(`${environment.apiUrl}${this.testRoute}`);
    }

}