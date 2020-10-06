import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent implements OnInit {
  title = 'client';
  lat = 14.881184;
  lng = 102.019734;
  ll = 14;
  ln =102;
  constructor() { }

  ngOnInit(): void {
  }

}



