import "./Login.scss";

export const Login = () => {
  const imageMoreUrl =
    "https://images.unsplash.com/photo-1572025442348-511bdcae389b?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D";

  return (
    <div className="login-container">
      <div className="login-wrapper">
        <div
          className="login-more"
          style={{
            backgroundImage: `url(${imageMoreUrl})`,
          }}
        ></div>
        <div className="login-form flex items-center flex-col justify-center">
          <h3>Login to continue</h3>
          <form>
            <div className="mb-3">
              <label>username</label>
              <input type="text" />
            </div>
            <div>
              <label>password</label>
              <input type="text" />
            </div>
          </form>
        </div>
      </div>
    </div>
  );
};
