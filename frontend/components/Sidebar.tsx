import React from 'react'
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
// import { useSession, signIn, signOut } from "next-auth/react"

function Sidebar() {
  // const { data: session } = useSession()
  // console.log('session', session)
  const session = true

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
                // onClick={session ? signOut : signIn }
                // title={session ? 'Sign Out' : 'Sign In'} />
                // onClick={session ? signOut : signIn }
                title={session ? 'Sign Out' : 'Sign In'} />
        <SidebarRow Icon={DotsCircleHorizontalIcon} title='More' />
    </div>
  )
}

export default Sidebar