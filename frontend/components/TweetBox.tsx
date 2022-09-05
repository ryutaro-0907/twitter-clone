import React, { Dispatch, SetStateAction, useRef, useState } from 'react';
import {
    CalendarIcon,
    EmojiHappyIcon,
    LocationMarkerIcon,
    PhotographIcon,
    SearchCircleIcon,
} from "@heroicons/react/outline";
import toast from 'react-hot-toast';

import { Tweet, TweetBody } from '../typings';
import { fetchTweets } from '../utils/tweet_handler';
import { store } from '../redux/store';


interface Props {
    setTweets: Dispatch<SetStateAction<Tweet[]>>
}

function TweetBox({ setTweets }: Props) {
    const [input, setInput] = useState<string>("");
    const [image, setImage] = useState<string>("");

    // const { data: session } = useSession();
    const session = store.getState().user.is_login
    const stateUsername = store.getState().user.username

    const [imageUrlBoxIsOpen, setImageUrlBoxIsOpen] = useState<boolean>(false)
    const imageInputRef = useRef<HTMLInputElement>(null);

    const addImageToTweet = (e: React.MouseEvent<HTMLButtonElement, globalThis.MouseEvent>) => {
        e.preventDefault();

        if (!imageInputRef.current?.value) return;

        setImage(imageInputRef.current?.value);
        imageInputRef.current.value = '';
        setImageUrlBoxIsOpen(false);
    }

    const postTweet = async () => {
        const tweetInfo: TweetBody = {
            user_id: 1,
            text: input,
            username: stateUsername,
            profile_image: 'https://links.papareact.com/gll',
            // username: session?.user?.name || 'Unknown user',
            // profileImage: session?.user?.image || 'https://links.papareact.com/gll',
            // images: image,
        }

        const result = await fetch('http://localhost:8080/server/tweets', {
            body: JSON.stringify(tweetInfo),
            method: 'POST',
            headers: {
                'Content-type': 'application/json',
              },
        })

        console.log('result', result)

        const json = await result.json();
        const data = await fetch('http://localhost:8080/server/tweets')
        const newTweets: Tweet[] = await data.json()
        setTweets(newTweets);

        toast('Tweet posted successfully', {
            icon: '🚀'
        })

        return json
    }

    const handleSubmit = (e: React.MouseEvent<HTMLButtonElement,
        MouseEvent>) => {
            console.log('handleSubmit called')
            e.preventDefault();

            postTweet();

            setInput('');
            setImage('');
            setImageUrlBoxIsOpen(false)
            console.log('handleSubmit finished successfully')
    }

    return (
    <div className="flex space-x-2 p-5">
        <img
            className="h-14 w-14 object-cover
            rounded-full mt-4 "
            // src={session?.user?.image || "https://links.papareact.com/gll"}
            src="https://links.papareact.com/gll"
            alt=""
        />
        <div className="flex flex-1 items-center pl-2">
            <form className="flex flex-1 flex-col">
                <input
                    value={input}
                    onChange={e => setInput(e.target.value)}
                    type="text"
                    placeholder="What's happening?"
                    className="h-24 w-full text-xl outline-none
                                placeholder:text-xl" />
                <div className="flex items-center">
                    <div className="flex flex-1 space-x-2 text-twitter">
                        <PhotographIcon
                            onClick={() => setImageUrlBoxIsOpen
                            (!imageUrlBoxIsOpen)}
                            className="h-5 w-5
                            cursor-pointer transition-transform duration-150 ease-out
                            hover:scale-150"
                        />
                        <SearchCircleIcon className="h-5 w-5" />
                        <EmojiHappyIcon className="h-5 w-5" />
                        <CalendarIcon className="h-5 w-5" />
                        <LocationMarkerIcon className="h-5 w-5" />

                    </div>
                    <button
                        onClick={handleSubmit}
                        disabled={!input || !session}
                        className="rounded-full bg-twitter text-white
                                font-bold px-5 py-2 disabled:opacity-40">
                        Tweet
                    </button>
                </div>
                {imageUrlBoxIsOpen && (
                    <form className="rounded-lg mt-5 flex bg-twitter/80
                    py-2 px-4">
                        <input
                            ref={imageInputRef}
                            className="flex-1 bg-transparent p-2 text-white
                            outline-none placeholder:text-white"
                            type="text"
                            placeholder='Enter image url'/>
                        <button
                            type="submit"
                            onClick={addImageToTweet}
                            className="font-bold text-white"
                        >   Add image
                        </button>
                    </form>
                )}

                {image && (
                    <img
                        className="mt-10 h-40 w-full rounded-xl
                        object-contain shadow-lg"
                        src={image}
                        alt=''
                    />
                )}
            </form>
        </div>
    </div>
  )
}

export default TweetBox