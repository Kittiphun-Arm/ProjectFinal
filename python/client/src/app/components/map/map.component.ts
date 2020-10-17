import { Component, OnInit } from '@angular/core';
import { Map } from './map'
import { MapService } from '../../service/map.service'
import { HttpClient } from '@angular/common/http'
import { Router } from '@angular/router';
@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent implements OnInit {
  map: Map[]
  lat = 14.881184;
  lng = 102.019734;
  show: boolean = true;
  constructor(private mapService: MapService,private router:Router,private http: HttpClient) { }

  ngOnInit(): void {
    this.getMap()
  }
  getMap(): void {
    this.mapService.getMap().subscribe(map => (this.map = map))
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
  onClick(){
    this.show = !this.show
  }
}



