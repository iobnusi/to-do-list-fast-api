export interface LoginRequest {
  username: string;
  password: string;
}

export interface RegisterRequest {
  name: string;
  password: string;
}

export interface AuthResponse {
  access_token: string;
  token_type: string;
}

