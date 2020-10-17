import { Component, OnInit } from '@angular/core';
import { Showdata } from './showdata'
import { ShowdataService } from '../../service/showdata.service'
import { HttpClient } from '@angular/common/http'
import { Router } from '@angular/router';
@Component({
  selector: 'app-showdata',
  templateUrl: './showdata.component.html',
  styleUrls: ['./showdata.component.css']
})
export class ShowdataComponent implements OnInit {
  showdata: Showdata[]
  lat = 14.881184;
  lng = 102.019734;
  lt = 14;
  lg = 102;
  constructor(private showdataService: ShowdataService,private router:Router,private http: HttpClient) { }

  ngOnInit(): void {
    this.getShowdata()
  }
  getShowdata (): void {
    this.showdataService.getShowdata().subscribe(showdata => (this.showdata = showdata))
}
showdataa(){
  this.router.navigate(['/showdata']);
}
home(){
  this.router.navigate(['/home']);
}
mappa(){
  this.router.navigate(['/map']);
}
}
