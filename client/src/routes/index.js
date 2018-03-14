// We only need to import the modules necessary for initial render
import CoreLayout from '../layouts/PageLayout/PageLayout'
import AdminLayout from './../layouts/AdminLayout/AdminLayout'
import NotLayout from './../layouts/NotLayout/NotLayout'
import CounterRoute from './Counter'
import Home from './Home'
import Login from './Login'

export const createRoutes = (store) => ([
  {
    path: '/admin',
    component: AdminLayout,
    indexRoute: Home,
    childRoutes: [
      CounterRoute(store)
    ]
  },
  {
    path: '/auth',
    component: NotLayout,
    indexRoute: Login,
    childRoutes: [
      CounterRoute(store)
    ]
  },
  {
    path: '/',
    component: CoreLayout,
    indexRoute: Home,
    childRoutes: [
      CounterRoute(store)
    ]
  }
])

export default createRoutes
