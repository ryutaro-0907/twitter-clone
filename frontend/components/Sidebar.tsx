import React from 'react'
import { useDispatch, useSelector } from 'react-redux';
import { useRouter } from 'next/router'

import {
    BellIcon,
    HashtagIcon,
    BookmarkIcon,
    CollectionIcon,
    DotsCircleHorizontalIcon,
    MailIcon,
    UserIcon,
    HomeIcon,
} from '@heroicons/react/outline'
import SidebarRow from './SidebarRow'

import { store } from '../redux/store'
import { userSlice } from '../redux/userSlice'


function Sidebar() {
  // const { data: session } = useSession()
  // console.log('session', session)
  const is_login = store.getState().user.is_login
  const router = useRouter()
  const dispatch = useDispatch()
  const { logout } = userSlice.actions;


  const signIn = () => {
    // e.preventDefault()
    router.push('/signup')
  }

  const signOut = () => {
    // e.preventDefault()
    dispatch(logout())
    router.push('/')
  }

  return (
    <div className='col-span-2 flex flex-col items-center px-4
    md:items-start'>
        <img className='m-3 h-10 w-10' src='https://links.papareact.com/drq' alt=''></img>
        <SidebarRow Icon={HomeIcon} title='Home' />
        <SidebarRow Icon={HashtagIcon} title='Explore' />
        <SidebarRow Icon={BellIcon} title='Notifications' />
        <SidebarRow Icon={MailIcon} title='Messages' />
        <SidebarRow Icon={BookmarkIcon} title='Bookmarks' />
        <SidebarRow Icon={CollectionIcon} title='Lists' />
        <SidebarRow
                Icon={UserIcon}
                onClick={is_login ? signOut : signIn }
                title={is_login ? 'Sign Out' : 'Sign In'} />
        <SidebarRow Icon={DotsCircleHorizontalIcon} title='More' />
    </div>
  )
}

export default Sidebar