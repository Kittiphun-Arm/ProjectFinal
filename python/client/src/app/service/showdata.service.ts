import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Observable } from 'rxjs';
import { Showdata } from '../components/showdata/showdata';


const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};
@Injectable({ providedIn: 'root' })
export class ShowdataService {
  private dataUrl = 'http://localhost:5000';  // URL to REST API
  constructor(private http: HttpClient) { }

  getShowdata(): Observable<Showdata[]> {
    return this.http.get<Showdata[]>(this.dataUrl + '/dataDisaster');
  }
  getShowdat(id: string): Observable<any> {
    const url = `${this.dataUrl}/user/${id}`;
    return this.http.get<Showdata>(url);
  }
}
