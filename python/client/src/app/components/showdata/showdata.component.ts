import { Component, OnInit } from '@angular/core';
import { Showdata } from './showdata'
import { ShowdataService } from '../../service/showdata.service'
import { HttpClient } from '@angular/common/http'
@Component({
  selector: 'app-showdata',
  templateUrl: './showdata.component.html',
  styleUrls: ['./showdata.component.css']
})
export class ShowdataComponent implements OnInit {
  showdata: Showdata[]

  constructor(private showdataService: ShowdataService,private http: HttpClient) { }

  ngOnInit(): void {
    this.getShowdata()
  }
  getShowdata (): void {
    this.showdataService.getShowdata().subscribe(showdata => (this.showdata = showdata))
}

}
