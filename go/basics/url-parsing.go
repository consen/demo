package main

import (
	"fmt"
	"net"
	"net/url"
)

func main() {
	// We’ll parse this example URL, which includes
	// a scheme, authentication info, host, port, path, query params, and query fragment.
	s := "postgres://user:pass@host.com:5432/path?k=v#f"
	//s := "postgres://user:pass@host.com:5432\x13/path?k=v#f"	// invalid character "\x13" in host name

	u, err := url.Parse(s)
	if err != nil {
		panic(err)
	}

	fmt.Println(u.Scheme)

	fmt.Println(u.User)
	fmt.Println(u.User.Username())
	p, _ := u.User.Password()
	fmt.Println(p)

	fmt.Println(u.Host)
	host, port, _ := net.SplitHostPort(u.Host)
	fmt.Println(host)
	fmt.Println(port)

	fmt.Println(u.Path)
	fmt.Println(u.Fragment)

	fmt.Println(u.RawQuery)
	m, _ := url.ParseQuery(u.RawQuery)
	fmt.Println(m)
	fmt.Println(m["k"][0])
}
