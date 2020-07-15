import Cookie from "js-cookie";

export default function({ $axios }) {
  if (process.server) {
    return;
  }

  $axios.interceptors.request.use(request => {
    const token = Cookie.get("voynich_jwt");

    if (token) {
      request.headers.common.Authorization = "Token " + token;
    }
    return request;
  });
}
