import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { MapComponent } from './components/map/map.component';
import { ShowdataComponent } from './components/showdata/showdata.component';

const routes: Routes = [
  {path: 'home' ,component:HomeComponent},
  {path: 'map' ,component:MapComponent},
  {path: 'showdata' ,component:ShowdataComponent},
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
