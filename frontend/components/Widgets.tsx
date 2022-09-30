import React from 'react';

import { SearchIcon } from "@heroicons/react/outline";
import { TwitterTimelineEmbed } from 'react-twitter-embed';
function Widgets() {
  return (
    <div className="col-span-2 mt-5 hidden px-2 lg:inline">
        {/* Search box */}
        <div className="flex items-center space-x-2 rounded-full bg-gray-200
        p-3 ">
            <SearchIcon className='h-5 w-5 text-gray-400'/>
            <input type='text' className='flex-1 bg-transparent outline-none' placeholder='Search Twitter'></input>
        </div>

        <TwitterTimelineEmbed
         sourceType='profile'
         screenName='ryulovepython'
         options={{height:400}}/>
    </div>
  )
}

export default Widgets;