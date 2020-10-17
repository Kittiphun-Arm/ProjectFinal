import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Observable } from 'rxjs';
import { Map } from '../components/map/map';
const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};
@Injectable({
  providedIn: 'root'
})
export class MapService {
  private dataUrl = 'http://localhost:5000';  // URL to REST API
  constructor(private http: HttpClient) { }

  getMap(): Observable<Map[]> {
    return this.http.get<Map[]>(this.dataUrl + '/dataDisaster');
  }
  getMapa(id: string): Observable<any> {
    const url = `${this.dataUrl}/user/${id}`;
    return this.http.get<Map>(url);
  }
}


