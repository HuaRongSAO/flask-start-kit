// We only need to import the modules necessary for initial render
import CoreLayout from '../layouts/PageLayout/PageLayout'
import AdminLayout from './../layouts/AdminLayout/AdminLayout'
import NotLayout from './../layouts/NotLayout/NotLayout'
import Home from './Home'
import CounterRoute from './Counter'

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
    path: '/login',
    component: NotLayout,
    indexRoute: Home,
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
