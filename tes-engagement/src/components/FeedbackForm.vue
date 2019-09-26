<template>
  <div class="container">
    <!-- START ARTICLE FEED -->
    <section class="articles">
      <div class="column is-8 is-offset-2">
        <!-- START ARTICLE -->
        <div class="card article">
          <div class="card-content">
            <div class="media">
              <div class="media-content has-text-centered">
                <p class="title article-title">TES Engagement Anonymous Feedback</p>
              </div>
            </div>
            <div class="content article-body">
              <p>In the interest of driving Racker engagement, preventing attrition, and restoring pride in being a Racker, the R4R team invites you to anonymously submit constructive criticism, concerns, and suggestions for improvement.</p>
              <p>These comments will be reviewed by frontline Rackers in the R4R group, NOT leadership, and used collectively to work towards the goals listed above.</p>
              <h3 class="has-text-centered">Give us your thoughts and feedback</h3>
              <b-field>
                <b-input
                  v-model=comment
                  maxlength="2000"
                  type="textarea"
                />
              </b-field>
              <div class="field">
                <b-switch v-model="contact">
                  Would you like to be contacted?
                </b-switch>
              </div>
              <b-field v-if="contact">
                <b-input v-model="email" placeholder="Email" type="email"></b-input>
              </b-field>
              <b-button :disabled="!allowSubmit" @click.stop.prevent="submitForm" type="is-primary">Submit</b-button>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
<script>
export default {
  name: 'FeedbackForm',
  data() {
    return {
      comment: '',
      email: '',
      contact: false,
      allowSubmit: true,
    };
  },
  methods: {
    async submitForm() {
      this.allowSubmit = false;
      let self = this;
      fetch('/comment', {
        method: 'post',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({comment: self.comment, email: self.email})
      }).then(function(response) {
        if (response.status == 200) {
          self.success();
        } else {
          self.failed();
        }
      }).then(function() {
        self.allowSubmit = true;
      });
    },
    success() {
      this.$buefy.snackbar.open({
        message: 'Your comment has been submitted successfully.  Thank you.',
        type: 'is-success',
        position: 'is-top',
        actionText: 'Close',
        indefinite: true,
      });
      this.comment = '';
      this.email = '';
    },
    failed() {
      this.$buefy.snackbar.open({
        message: 'Your comment submssion failed.  Please try again.',
        type: 'is-danger',
        position: 'is-top',
        actionText: 'Close',
        indefinite: true,
      });
    },
  },
}
</script>
