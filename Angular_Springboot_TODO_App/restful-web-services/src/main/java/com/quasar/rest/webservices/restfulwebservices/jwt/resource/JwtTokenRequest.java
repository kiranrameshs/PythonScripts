package com.quasar.rest.webservices.restfulwebservices.jwt.resource;

import java.io.Serializable;

public class JwtTokenRequest implements Serializable {

	private static final long serialVersionUID = -5616176897013108345L;

	private String username;
	private String password;
//
//	{
//		"token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJraXJhbiIsImV4cCI6MTU5ODU1NTQzMCwiaWF0IjoxNTk3OTUwNjMwfQ.25UgKYGVakdiDC_WwFJJUiL2Re76PTgtDdrnZz2qhYam3gsEMqVFtdam5nwBO-WhKbGAKAJACY4zNBR9sxzq3w"
//	}
	public JwtTokenRequest() {
		super();
	}

	public JwtTokenRequest(String username, String password) {
		this.setUsername(username);
		this.setPassword(password);
	}

	public String getUsername() {
		return this.username;
	}

	public void setUsername(String username) {
		this.username = username;
	}

	public String getPassword() {
		return this.password;
	}

	public void setPassword(String password) {
		this.password = password;
	}
}
