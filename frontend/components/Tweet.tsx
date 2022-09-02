import { Tweet, Comment, CommentBody } from '../typings';
import TimeAgo from 'react-timeago';

import {
    ChatAlt2Icon,
    HeartIcon,
    SwitchHorizontalIcon,
    UploadIcon,
} from '@heroicons/react/outline';

import { useState, useEffect } from 'react';
import { useSession } from 'next-auth/react';
import toast from 'react-hot-toast';
import internal from 'stream';


interface Props {
    tweet: Tweet
}

function Tweet({ tweet } : Props) {

  const [comments, setComments] = useState<Comment[]>([])
  const [commentBoxVisible, setCommentBoxVisible] = useState<boolean>(false);
  const [input, setInput] = useState<string>('');

//   const { data: session } = useSession();
  const session = true
  const fetchCommentsById = async (tweet_id: number) => {
    try {
      const data = await fetch(`http://localhost:8080/server/comments?tweet_id=${tweet_id}`)
      const comments: Comment[] = await data.json()
      console.log('tweets fetched succesfully;')

      return comments
    } catch (err) {
      throw new Error('error fetching tweet: ' + err!)
  }}

  const refreshComments = async () => {
    const comments: Comment[] = await fetchCommentsById(tweet.id);
    setComments(comments);
  }

  useEffect(() => {
      refreshComments();
  }, []);


  const postComment = async () => {
    const commentInfo: CommentBody = {
        comment: input,
        username: 'test user',
        profile_image: 'https://links.papareact.com/gll',
        user_id: 1,
        tweet_id: tweet.id,
        // username: session?.user?.name || 'Unknown user',
        // profileImage: session?.user?.image || 'https://links.papareact.com/gll',
        // tweetId: tweet._id,
    }

    const result = await fetch(`http://localhost:8080/server/comments`, {
        body: JSON.stringify(commentInfo),
        headers: {
            'Content-type': 'application/json',
          },
        method: 'POST',
    })

    console.log('fetching comment esult', result)

    const json = await result.json();

    const newComments = await fetchCommentsById(tweet.id);
    setComments(newComments);

    toast('Comment posted successfully', {
        icon: '🚀'
    })

    return json
}


  const handleSubmitForComment = (e: React.FormEvent<HTMLElement>) => {
      e.preventDefault();

      postComment();

      setInput('');
      setComments([]);
      setCommentBoxVisible(false);

  }

  return (
    <div className="flex flex-col space-x-3 border-y
                    border-gray-100 p-5"
     >
        <div className="flex space-x-3">
            <img
                className="h-10 w-10 rounded-full object-cover"
                src={tweet.profile_image} alt=""
            />
            <div>
                <div className='flex items-center space-x-1'>
                    <p className='mr-1 font-bold'>{tweet.username}</p>
                    <p className='hidden text-sm text-gray-500
                                    sm:inline'>
                        @{tweet.username.replace(/\s+/g, '').toLowerCase()}.
                    </p>

                    <TimeAgo
                        className='text-sm text-gray-500'
                        date={tweet.created_at}
                     />
                </div>
                <p className='pt-1'>{tweet.text}</p>

                {
                    tweet.images && (
                        <img
                            className="m-5 ml-0 mb-1 max-h-60
                                        rounded-lg object-cover shadow-sm"
                            src={tweet.images} alt=''
                        />
                    )
                }
            </div>
        </div>
        <div  className='mt-5 flex justify-between'>
            <div
                onClick={() => session && setCommentBoxVisible(!commentBoxVisible)}
                className='flex cursor-pointer items-center space-x-3 text-gray-400'>
                <ChatAlt2Icon
                    className="h-5 w-5" />
                <p> {comments.length} </p>
            </div>
            <div className='flex cursor-pointer items-center space-x-3 text-gray-400'>
                <SwitchHorizontalIcon className="h-5 w-5" />
            </div>
            <div className='flex cursor-pointer items-center space-x-3 text-gray-400'>
                <HeartIcon className="h-5 w-5" />
            </div>
            <div className='flex cursor-pointer items-center space-x-3 text-gray-400'>
                <UploadIcon className="h-5 w-5" />
            </div>
        </div>

        {commentBoxVisible && (
            <form
                className="mt-3 flex space-x-3">
                <input
                    onChange={(e) => setInput(e.target.value)}
                    value={input}
                    className="flex-1 rounded-lg
                    bg-gray-100 p-2 outline-none"
                    type="text"
                    placeholder='write a comment' />
                <button
                    disabled={!input}
                    onClick={handleSubmitForComment}
                    type="submit"
                    className="text-twitter
                        disabled:text-gray-200" >
                        Post
                </button>
            </form>
        )}

        {comments?.length > 0  && (
            <div className='my-2 mt-5 max-h-44 space-y-5 overflow-y-scroll border-t
            border-gray-100 p-5'>
                {comments.map((comment) => (
                    <div key={comment.id} className='relative flex space-x-2'>
                        <hr className='absolute left-5 top-10 h-8 border-x
                        border-twitter/30'  />
                        <img
                            src={comment.profile_image}
                            className='mt-5 h-7 w-7
                                rounded-full object-cover'
                            alt=''
                        />
                        <div>
                            <div className='flex items-center space-x-1'>
                                <p className='mr-1 font-bold'>{comment.username}</p>
                                <p className='hidden text-sm text-gray-500 lg:inline'>
                                    @{comment.username.replace(/\s+/g, '').toLowerCase()}.
                                </p>
                                <TimeAgo
                                    className="text-sm text-gray-500"
                                    date={comment.created_at}
                                />
                            </div>
                            <p>
                            {comment.comment}
                            </p>
                        </div>
                    </div>
                ))}
            </div>
        )}
    </div>
  )
}

export default Tweet;
