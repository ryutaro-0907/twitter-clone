import { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useRouter } from 'next/router'

import { userSlice } from '../redux/userSlice';
import { store } from '../redux/store';
interface UserCreate {
    username: string;
    // email: string;
    password: string;
}
function signup() {
    // const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [username, setUsername] = useState('')

    const router = useRouter()

    const dispatch = useDispatch();
    const { login, logout, setStateUsername, setStateEmail } = userSlice.actions;
    const is_login = store.getState().user.is_login
    const stateUsername = store.getState().user.username

    console.log(stateUsername, 'logged in:', is_login)

    const createUserAndReturnSessionIfSuccess = (e) => {
        console.log('createing user')

        e.preventDefault();

        const userCreate: UserCreate = {
            username: username,
            // email: email,
            password: password,
        }

        const res  = fetch('http://localhost:8081/api/v1/auth/register', {
            body: JSON.stringify(userCreate),
            method: 'POST',
            headers: {
                'Content-type': 'application/json',
              },
        }).then(response => {
            dispatch(login())
            // dispatch(setStateEmail(email))
            dispatch(setStateUsername(username))
            router.push('/login')

        }).catch(() => alert('Email is already taken, please login'))
    }

  return (
    <div>
        <div className="bg-grey-lighter min-h-screen flex flex-col">
            <div className="container max-w-sm mx-auto flex-1
            flex flex-col items-center justify-center px-2">
                <div className="bg-white px-6 py-8 rounded shadow-md text-black w-full">
                <h1 className="mb-8 text3xl text-center">Sign up</h1>
                <form className="">
                    <input
                        value={username}
                        onChange={e => setUsername(e.target.value)}
                        type="text"
                        className="block border border-grey-light w-full p-3 rounded mb-4"
                        name="username"
                        placeholder="Username"
                         />
                    {/* <input
                        value={email}
                        onChange={e => setEmail(e.target.value)}
                        type="text"
                        className="block border border-grey-light w-full p-3 rounded mb-4"
                        name="email"
                        placeholder="Email Address"
                         /> */}
                    <input
                        value={password}
                        onChange={e => setPassword(e.target.value)}
                        type="password"
                        className="block border border-gray-light w-full p-3 rounded mb-4"
                        name="password"
                        placeholder="Password"
                         />
                    <button
                        type="submit"
                        onClick={createUserAndReturnSessionIfSuccess}
                        // disabled={!username || !email || !password}
                        disabled={!username || !password}
                        className="w-full text-center py-3 rounded
                         bg-blue-500 text-white
                         hober:bg-blue-200 focus:outline-none my-1">
                            Create Account
                    </button>
                </form>
                    <div className="text-center text-sm text-grey-dark mt-4">
                        By signing up, you agree to <a className="" href="">the Terms of Service</a> and Privacy Policy
                    </div>

                </div>
                <div className="text-grey-dark mt-6">
                    Aleady have an account?
                    <a className="no-underline border-b border-blue text-blue-600" href="../login"> Log in</a>
                </div>
            </div>
        </div>
    </div>
  )
}

export default signup