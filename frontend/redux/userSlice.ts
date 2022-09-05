import { createSlice } from '@reduxjs/toolkit';

export const userSlice = createSlice({
  name: 'user',
  initialState: {
    is_login: false,
    email: '',
    username: '',
  },
  reducers: {
    login: (state) => {
      state.is_login = true;
    },
    setStateEmail: (state, action) => {
        state.email = action.payload
    },
    setStateUsername: (state, action) => {
        state.username = action.payload
    },
    logout: (state) => {
      state.is_login = false;
      state.email = '';
      state.username = '';
    },
  },
});

export const { login, logout } = userSlice.actions;

export default userSlice.reducer;