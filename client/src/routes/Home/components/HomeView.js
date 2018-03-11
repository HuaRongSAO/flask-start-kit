import React from 'react'
import DuckImage from '../assets/Duck.jpg'
import './HomeView.scss'

export const HomeView = () => (
  <div>
    <h1 className='text-center'>Welcome!</h1>
    <img alt='This is a duck, because Redux!' className='duck' src={ DuckImage }/>
  </div>
)

export default HomeView
