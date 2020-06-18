package main

import (
	"context"
	"log"
	"net/http"
	"os"
	"strconv"
	"time"

	"github.com/bradleyfalzon/ghinstallation"
	"github.com/google/go-github/v29/github"
)

const InstallationID = os.Getenv("INSTALLATION_ID")
const RepoOwner = "Yashikab"
const Repo = "drone_yml_practice"
const IssueNumber = 1

func main() {
	appID, err := strconv.ParseInt(os.Getenv("GITHUB_APP_ID"), 10, 64)
	if err != nil {
		log.Fatal(err)
	}

	tr := http.DefaultTransport
	itr, err := ghinstallation.NewKeyFromFile(tr, appID, InstallationID, "private-key.pem")
	if err != nil {
		log.Fatal(err)
	}

	client := github.NewClient(&http.Client{
		Transport: itr,
		Timeout:   5 * time.Second,
	})

	ctx := context.Background()

	body := "hello"
	comment := &github.IssueComment{
		Body: &body,
	}
	if _, _, err := client.Issues.CreateComment(ctx, RepoOwner, Repo, IssueNumber, comment); err != nil {
		log.Fatal(err)
	}
}
