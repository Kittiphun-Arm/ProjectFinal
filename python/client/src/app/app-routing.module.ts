import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { DataDisasterComponent } from './components/data-disaster/data-disaster.component';
import { HomeComponent } from './components/home/home.component';
import { MapComponent } from './components/map/map.component';
import { MenuComponent } from './components/menu/menu.component';
import { ShowdataComponent } from './components/showdata/showdata.component';

const routes: Routes = [
  {path: 'home' ,component:HomeComponent},
  {path: 'map' ,component:MapComponent},
  {path: 'menu', component:MenuComponent},
  {path: 'showdata' ,component:ShowdataComponent},
  {path: 'data-disaster' ,component:DataDisasterComponent},
  {path: '',
    redirectTo: 'home',
    pathMatch: 'full'
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
