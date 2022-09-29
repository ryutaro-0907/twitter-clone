import { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useRouter } from 'next/router'

import { userSlice } from '../redux/userSlice';
import { store } from '../redux/store';

interface UserLogin {
    // email: string;
    username: string
    password: string;
}

function login() {
    // const [email, setEmail] = useState<string>('')
    const [username, setUsername] = useState<string>('')
    const [password, setPassword] = useState<string>('')

    const router = useRouter()

    const dispatch = useDispatch();
    const { login, setStateUsername, setStateEmail } = userSlice.actions;

    const userLogin = async (e) => {
        e.preventDefault();

        const userLogin: UserLogin = {
            // email: email,
            username: username,
            password: password,
        }

        const res  = fetch('http://localhost:8081/api/v1/auth/login', {
            body: JSON.stringify(userLogin),
            method: 'POST',
            headers: {
                'Content-type': 'application/json',
              },

        }).then(response => {
            const data = response.json()
            console.log(data)

            dispatch(login())
            // dispatch(setStateEmail(email))
            dispatch(setStateUsername(username))
            dispatch(setStateUsername('afdsfsaf'))

            router.push('/')

        }).catch(res => {
            console.log('Failed to login', res)
            alert('Email is Password is incorrect please try again.' )
        })
    }

    return (
      <div>
          <div className="bg-grey-lighter min-h-screen flex flex-col">
              <div className="container max-w-sm mx-auto flex-1
              flex flex-col items-center justify-center px-2">
                  <div className="bg-white px-6 py-8 rounded shadow-md text-black w-full">
                  <h1 className="mb-8 text3xl text-center">Log in</h1>
                  <form className="">
                      <input
                          value={username}
                          onChange={e => setUsername(e.target.value)}
                          type="text"
                          className="block border border-grey-light w-full p-3 rounded mb-4"
                          name="username"
                          placeholder="Username"
                           />
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
                          disabled={!username || !password}
                          onClick={userLogin}
                          className="w-full text-center py-3 rounded
                           bg-blue-500 text-white
                           hober:bg-blue-200 focus:outline-none my-1">
                             Log in
                      </button>
                  </form>
                  </div>
                  <div className="text-grey-dark mt-6">
                      Don't have an account?
                      <a className="no-underline border-b border-blue text-blue-600" href="../signup"> Sign up!</a>
                  </div>
              </div>
          </div>
      </div>
    )
  }

  export default login