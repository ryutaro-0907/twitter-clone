import axios from 'axios';

export const client = axios.create({
    // baseURL: process.env.BASE_URL,
    baseURL: 'http://0.0.0.0:8000',
    headers: { 'Content-Type': 'application/json; charset=utf-8', Accept: 'application/json' },
    // transformRequest: [
    //     // TODO: add method to convert data from CamelCase to SnakeCase.
    //     (data: any, headers: any) => {
    //       //  FIXME
    //         // const snakeCase: any = {}
    //         // for (const [key, value] of Object.entries(data)) {
    //         //     let renamedKey = key.replace(/[A-Z]/g, letter => `_${letter.toLowerCase()}`);
    //         //     snakeCase[renamedKey] = value
    //         // }

    //         // TODO add this
    //         // const encryptedString = encryptPayload(JSON.stringify(data));
    //         // data = {
    //         //     SecretStuff: encryptedString,
    //         // };


    //         return JSON.stringify(data);
    //     },
    // ],
    // transformResponse: [
    //     (data: any) => {
    //       let resp;
    //       try {
    //         resp = JSON.parse(data);
    //       } catch (error) {
    //         throw Error(
    //           `[requestClient] Error parsingJSON data - ${JSON.stringify(
    //             error
    //           )}`
    //         );
    //       }
    //       if (resp.status === "success") {
    //         // const camelCase: any = {}

    //         // for (const [key, value] of Object.entries(resp.data)) {
    //         //     let renamedKey = key.replace(/([-_]\w)/g, g => g[1].toUpperCase())
    //         //     console.log(renamedKey)
    //         //     camelCase[renamedKey] = value
    //         // }
    //         // return camelCase;
    //         return resp.data
    //       } else {
    //         throw Error(`Request failed with reason -  ${data}`);
    //       }
    //     },
    //   ],
});
