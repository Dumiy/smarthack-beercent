import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from '../../../environments/environment';
import { Observable } from 'rxjs';

@Injectable({
    providedIn: 'root'
})
export class ProductService {
    productRoute: string = '/searchengine/search';
    httpOptions = {
        headers: new HttpHeaders({'Content-Type': 'application/json'})
        // headers: new HttpHeaders({ 'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'})
    }
    constructor(private http: HttpClient) {};

    //GET
    getProductsByKeys(obj: any): Observable<any> {
        return this.http.post(`${environment.apiUrl}${this.productRoute}`, obj, this.httpOptions);
    }

}