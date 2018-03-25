import React from 'react'
import { Menu } from 'antd'
import {browserHistory} from 'react-router'

const menuClick = ({item, key, keyPath}) => {
  if (key === 'layout') {
    console.log('退出登入')
    return
  }
  
  browserHistory.push(`/admin/${key}`)
}

const menu = (
  <Menu onClick={ menuClick }>
    <Menu.Item key="center">
      <a>个人中心</a>
    </Menu.Item>
    
    <Menu.Divider/>
    
    <Menu.Item key="layout">退出</Menu.Item>
  </Menu>
)

export default menu
